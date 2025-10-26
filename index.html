import transformers
import torch

class Chatbot:
    def __init__(self, model_name="gpt2"):
        self.tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
        self.model = transformers.AutoModelForCausalLM.from_pretrained(model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def generate_response(self, prompt, max_length=100):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long).to(self.device)

        output = self.model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            attention_mask=attention_mask,
            early_stopping=True
        )

        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response

    def chat(self):
        print("Chatbot: Halo! Saya adalah chatbot yang mirip dengan ChatGPT. Bagaimana saya bisa membantu Anda?")
        while True:
            user_input = input("Anda: ")
            if user_input.lower() == "berhenti":
                print("Chatbot: Sampai jumpa!")
                break

            prompt = f"Anda: {user_input}\nChatbot:"
            response = self.generate_response(prompt)
            print("Chatbot:", response)

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chat()
