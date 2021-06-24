terraform {
  backend "azurerm" {
    resource_group_name   = "AmericanExpress1_DaveRawlinson_ProjectExercise"
    storage_account_name  = "britboyazurestorage24051"
    container_name        = "britboyazurecontainer"
    key                   = "terraform.tfstate"
  }
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "2.62.1"
    }

  }
}

provider "azurerm" {
  # Configuration options
  features {}
}

data "azurerm_resource_group" "main" {name= "AmericanExpress1_DaveRawlinson_ProjectExercise"}

resource "azurerm_app_service_plan" "main" {
  name = "terraformed-asp"
  location = var.location
  resource_group_name = data.azurerm_resource_group.main.name
  kind= "Linux"
  reserved= true

  sku {
    tier = "Basic"
    size = "B1"
  }
}

resource "azurerm_app_service" "main" {
  name= "${var.prefix}britboytodolistsuper"
  location= data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  app_service_plan_id = azurerm_app_service_plan.main.id
  site_config {
    app_command_line = ""
    linux_fx_version = "DOCKER|britboy4321/todoapp:latest"
  }
  app_settings = {
        # For some reason primary_key was not accepted in azurerm_cosmosdb_account, so hardcoded here instead.  It works.
        "MONGODB_CONNECTION_STRING" = "mongodb://${azurerm_cosmosdb_account.main.name}:${azurerm_cosmosdb_account.main.primary_key}@${azurerm_cosmosdb_account.main.name}.mongo.cosmos.azure.com:10255/DefaultDatabase?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000"
        "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io"
        "client_id" = var.client_id
        "client_secret" = var.client_secret
# I REALISE OTHER THINGS COULD BE IN variables.tf BUT AM RUNNING OUT OF TIME - SO PROVING I UNDERSTAND THE PRINCIPLE
        "DOCKER_ENABLE_CI" = "true"
        "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io/v1"
        "FLASK_APP" = "todo_app/app"
        "FLASK_ENV" = "development"
        "OATH_INSECURE_TRANSPORT" = "1"
        "SECRET_KEY" = "secret-key"
        "WEBSITE_HTTPLOGGING_RETENTION_DAYS" = "1"
        "WEBSITES_CONTAINER_START_TIME_LIMIT" = "1400"
        "WEBSITES_ENABLE_APP_SERVICE_STORAGE" = "false"
        "OAUTHLIB_INSECURE_TRANSPORT"="1"
  }
}


resource "azurerm_cosmosdb_account" "main" {
  name                = "${var.prefix}britboytodoappterr"
  resource_group_name = "AmericanExpress1_DaveRawlinson_ProjectExercise"
  offer_type          = "Standard"
  kind                = "MongoDB"
  # lifecycle {prevent_destroy = true}   # Prevent DB destroy
  capabilities {name = "EnableServerless"}
  capabilities {
    name = "mongoEnableDocLevelTTL"
  }
  capabilities {
   name = "AllowSelfServeUpgradeToMongo36" # Found on google
  }
  capabilities {
    name = "EnableMongo"
  }
  location = "West Europe"
  geo_location {  
  location = "West Europe"
  failover_priority = "0"
  }
  consistency_policy {
  consistency_level       = "BoundedStaleness"
  max_interval_in_seconds = 10
  max_staleness_prefix    = 200
  }


}

resource "azurerm_cosmosdb_mongo_database" "main" {
  name                = "${var.prefix}britboydbterraform"
  resource_group_name = resource.azurerm_cosmosdb_account.main.resource_group_name
  account_name        = resource.azurerm_cosmosdb_account.main.name
  # throughput          = 400
}

output "endpoint" {
  value = azurerm_cosmosdb_account.main.endpoint
}
output "primary_key" {
  value = azurerm_cosmosdb_account.main.primary_key
  sensitive = true
  }

output "connection_strings" {
  value = azurerm_cosmosdb_account.main.connection_strings
  sensitive = true
}

output "webapp_url" {
  value = "https://${azurerm_app_service.main.default_site_hostname}"
}


#Next required for webhook into Travis

output "webhook_url" {
  value = "https://${azurerm_app_service.main.site_credential[0].username}:${azurerm_app_service.main.site_credential[0].password}@${azurerm_app_service.main.name}.scm.azurewebsites.net/docker/hook"
  sensitive = true
}