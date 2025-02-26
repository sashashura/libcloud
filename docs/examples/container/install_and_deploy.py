from libcloud.container.providers import get_driver
from libcloud.container.types import Provider

CREDS = ("user", "api key")

Cls = get_driver(Provider.DOCKER)
driver = Cls(*CREDS)

image = driver.install_image("tomcat:8.0")
container = driver.deploy_container("tomcat", image)

container.restart()
