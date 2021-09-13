from happytransformer import HappyGeneration, GENTrainArgs
# ---------------------------------------------------------
happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-125M")
train_args_1 = GENTrainArgs(save_preprocessed_data=True, save_preprocessed_data_path="data/preprocessed-data.json")
result = happy_gen.train("data/gen/GiftLab_Training_Data.txt", args=train_args_1)
    