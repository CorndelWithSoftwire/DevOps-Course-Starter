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
}

data "azurerm_resource_group" "main" {name= "AmericanExpress1_DaveRawlinson_ProjectExercise"}

resource "azurerm_app_service_plan" "main" {
  name= "terraformed-asp"
  location= data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  kind= "Linux"
  reserved= true

  sku {
    tier = "Basic"
    size = "B1"
  }
}

resource "azurerm_app_service" "main" {
  name= "britboytodolist"
  location= data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  app_service_plan_id = azurerm_app_service_plan.main.id
  site_config {
    app_command_line = ""
    linux_fx_version = "DOCKER|appsvcsample/python-helloworld:latest"
  }
  app_settings = {
    "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io"
  }
}

## UP TO HERE OK FOR HELLO_WORLD, NOW ON TO MY APP STUFF



resource "azurerm_cosmosdb_account" "main" {
  name                = "britboyaccountterraform"
  resource_group_name = "AmericanExpress1_DaveRawlinson_ProjectExercise"
  offer_type          = "Standard"
  kind                = "MongoDB"
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