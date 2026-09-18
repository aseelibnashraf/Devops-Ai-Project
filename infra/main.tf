terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
    }
  }
}

provider "docker" {
  host = "unix:///Users/aseel/.docker/run/docker.sock"
}

resource "docker_image" "app" {
  name = "devops-ai-app:latest"
}

resource "docker_container" "app" {
  name  = "devops-ai-app-container"
  image = docker_image.app.image_id
  ports {
    internal = 5000
    external = 5050
  }
}
