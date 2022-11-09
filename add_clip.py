from transformers import T5Tokenizer, T5EncoderModel, CLIPTokenizer, CLIPTextModel

version="openai/clip-vit-large-patch14"
test = CLIPTokenizer.from_pretrained(version)
