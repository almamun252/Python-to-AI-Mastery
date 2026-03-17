# Model Configuration using Dictionary
model_config = {
    "model_name": "ResNet50",
    "learning_rate": 0.001,
    "batch_size": 32,
    "optimizer": "Adam",
    "layers": [64, 128, 256, 512],
    "is_pretrained": True
}

# ---(Direct Assignment) ---

model_config["batch_size"] = 64         # Value update
model_config["epochs"] = 100            # Adding new key-value pair

print("Batch Size:", model_config["batch_size"])


# --- .update() method ---

new_settings = {
    "learning_rate": 0.0005,    # Value update
    "optimizer": "SGD",         # Value update
    "dropout_rate": 0.25,       # Adding new key-value pair
    "weight_decay": 1e-4        # Adding new key-value pair
}

model_config.update(new_settings)

print("Optimizer:", model_config["optimizer"])
print("Dropout Rate:", model_config["dropout_rate"])


# --- Final Model Configuration ---
print("\n--- Final Model Configuration ---")
import json
print(json.dumps(model_config, indent=4)) # Pretty print the dictionary for better readability