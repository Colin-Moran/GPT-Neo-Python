from happytransformer import HappyGeneration, GENSettings
from transformers.utils.dummy_pt_objects import MaxLengthCriteria
import os
happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-2.7B")

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
# Source - https://happytransformer.com/text-generation/settings/

default_settings = GENSettings(min_length=10, max_length=50, do_sample=False, early_stopping=True, num_beams=1, temperature=1.0, top_k=50, top_p=1.0, no_repeat_ngram_size=0, bad_words=None)
greedy_settings = GENSettings(no_repeat_ngram_size=2,  max_length=50)
beam_settings = GENSettings(num_beams=5,  max_length=10)
generic_sampling_settings = GENSettings(do_sample=True, top_k=0, temperature=0.7,  max_length=10)
top_k_sampling_settings = GENSettings(do_sample=True, top_k=50, temperature=0.7,  max_length=10)
top_p_sampling_settings = GENSettings(do_sample=True, top_k=0, top_p=0.8, temperature=0.7,  max_length=10)
bad_words_settings = GENSettings(bad_words = ["new form", "social"])

output = happy_gen.generate_text("These golf gloves are the perfect gift for the golf lover in your life.", args=greedy_settings)


# print(result)
with open('playground-result.txt', 'w') as f:
    f.write(output.text)