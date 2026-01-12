# this is a class: dog is the blueprint for creating dog objects

class Dog: 
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color


# creating an object of Dog class
doggy = Dog(name = "Gollu", breed = "Labrador")

# creating an object of Cat class
kitty = Cat(name = "Mimi", color = "White")

print(f"My dog's name is {doggy.name} and breed is {doggy.breed}")
print(f"My cat's name is {kitty.name} and color is {kitty.color}")


# -----------------------------------------------------------------------------
# Real world example for classes how we gonna use it in AI
class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

# Create different configurations
# Using positional for required arg, named for optional
dev_config = APIConfig("sk-dev-key", max_tokens=50)

# Using all named arguments (clearest)
prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

# Access the configuration
print(dev_config.model)        # gpt-3.5-turbo
print(prod_config.model)       # gpt-4
print(prod_config.max_tokens)  # 1000