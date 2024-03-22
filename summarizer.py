from transformers import T5ForConditionalGeneration, T5Tokenizer

def summarizer(text, max_summary_length, min_summary_length):
    # initialize the model architecture and weights
    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    # initialize the model tokenizer
    tokenizer = T5Tokenizer.from_pretrained("t5-base")

    # encode the text into tensor of integers using the appropriate tokenizer
    inputs = tokenizer.encode("summarize: " + text,
                              return_tensors="pt", max_length=512, truncation=True)

    # generate the summarization output
    outputs = model.generate(
        inputs,
        max_length=max_summary_length,
        min_length=min_summary_length,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True)
    summary = tokenizer.decode(outputs[0])
    summary = summary.replace("<pad>", "").replace("</s>", "")
    return summary

