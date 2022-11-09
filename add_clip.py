from transformers import T5Tokenizer, T5EncoderModel, CLIPTokenizer, CLIPTextModel

CLIPTokenizer.from_pretrained('openai/clip-vit-large-patch14', cache_dir='test', force_download=True)
CLIPTextModel.from_pretrained('openai/clip-vit-large-patch14', cache_dir='test', force_download=True)
