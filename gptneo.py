from happytransformer import HappyGeneration, GENSettings
from transformers.utils.dummy_pt_objects import MaxLengthCriteria

happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-1.3B")

# min_length - Minimum number of generated tokens
# max_length - Maximum number of generated tokens
# do_sample - When True, picks words based on their conditional probability
# early_stopping - When True, generation finishes if the EOS token is reached
# num_beams - Number of steps for each search path
# temperature - How sensitive the algorithm is to selecting low probability options
# top_k - How many potential answers are considered when performing sampling
# top_p - Min number of tokens are selected where their probabilities add up to top_p
# no_repeat_ngram_size - The size of an n-gram that cannot occur more than once. (0=infinity)
# bad_words - List of words/phrases that cannot be generated.

# These are the default settings
GENSettings(min_length=10, max_length=50, do_sample=False, early_stopping=False, num_beams=1, temperature=1.0, top_k=50, top_p=1.0, no_repeat_ngram_size=0, bad_words=None)
    
result = happy_gen.generate_text("Product Description: These golf gloves are the perfect gift for the golfer in your life.")
print(result)
print(result.text)
