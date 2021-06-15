terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "2.62.1"
    }
    # api_properties {
    # serverVersion = "4.0"
    # }
  }
}

provider "azurerm" {
  # Configuration options
  features {}
  backend "azurerm" {
    resource_group_name   = "AmericanExpress1_DaveRawlinson_ProjectExercise"
    storage_account_name  = "britboyazurestorage24051"
    container_name        = "britboyazurecontainer"
    key                   = "LaBye88Pf/inj0gfc0M7a/wL3/2U1ygMUYoT+h1RlyOEbLotz29rTqaemwXqBNj6/bCBzmpYD3kNXdCv+R5Zcw=="
  }
}

data "azurerm_resource_group" "main" {name= "AmericanExpress1_DaveRawlinson_ProjectExercise"}

resource "azurerm_app_service_plan" "main" {
  name = "terraformed-asp"
  # location= data.azurerm_resource_group.main.location
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
  name= "britboytodolistsuper"
  location= data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  app_service_plan_id = azurerm_app_service_plan.main.id
  site_config {
    app_command_line = ""
    #linux_fx_version = "DOCKER|appsvcsample/python-helloworld:latest"
    linux_fx_version = "DOCKER|britboy4321/todoapp:latest"
  }
  app_settings = {
        # For some reason primary_key was not accepted in azurerm_cosmosdb_account, so hardcoded here instead.  It works.
        "MONGODB_CONNECTION_STRING" = "mongodb://${azurerm_cosmosdb_account.main.name}:hEZ0qnr47mVOTTnrOYdquU7e4PzIKDPk9L8WOUF1ngK3CHtLVVYoscRcI4QGrbATVaffUciqbq2BOy8wRadVTg==@${azurerm_cosmosdb_account.main.name}.mongo.cosmos.azure.com:10255/DefaultDatabase?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000" 
        "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io"
        # "client_id" = "7b45e6f82314a24eae60"
        "client_id" = var.client_id
        #"client_secret" = "be07d5d4c655bf1d6765b061d3f32358aa560042"
        "client_secret" = var.client_secret
        "DOCKER_ENABLE_CI" = "true"
        "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io/v1"
        "FLASK_APP" = "todo_app/app"
        "FLASK_ENV" = "development"
        "key" = "308200bc2fe025877202575cdf262bd4"
        "OATH_INSECURE_TRANSPORT" = "1"
        "SECRET_KEY" = "secret-key"
        "WEBSITE_HTTPLOGGING_RETENTION_DAYS" = "1"
        "WEBSITES_CONTAINER_START_TIME_LIMIT" = "1400"
        "WEBSITES_ENABLE_APP_SERVICE_STORAGE" = "false"
        "OAUTHLIB_INSECURE_TRANSPORT"="1"
  }
}

## GOING TO EDIT THE ABOVE HELLO_WORLD, MOVE IT ON TO MY APP STUFF


resource "azurerm_cosmosdb_account" "main" {
  name                = "britboytodoappterr"
  # primary_key         = "v8o5nPzAho2xq1ddJ4ciGLGhQ15TO3MKyST4IMi4LYL5PaWy8SNiGEFR1S46Vr3yIDorL4Ra72BWyN5c2vjHBw=="
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
  name                = "britboydbterraform"
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

output "extra_variable" {
  value = "https://${azurerm_app_service.main.site_credential[0].username}:${azurerm_app_service.main.site_credential[0].password}@${azurerm_app_service.main.name}.scm.azurewebsites.net/docker/hook"
}