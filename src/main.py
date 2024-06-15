# Load model directly
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("klue/roberta-base")
model = AutoModelForMaskedLM.from_pretrained("klue/roberta-base")
#
# # Load model directly
# from transformers import AutoImageProcessor, AutoModelForImageClassification
#
# processor = AutoImageProcessor.from_pretrained("facebook/convnextv2-base-22k-224")
# model = AutoModelForImageClassification.from_pretrained("facebook/convnextv2-base-22k-224")