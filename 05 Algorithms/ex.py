import time





def run_quiz():
 quiz_data = {
 "Python kya hai?": "programming language",
 "List mutable hai ya immutable?": "mutable",
 "Dictionary mein data kis format mein store hota hai?": "key-value pair"
 }
 score = 0
 start_time = time.time()
 
 print("Welcome to the Python Quiz!\n")
 
 for question, answer in quiz_data.items():
    print(question)
    user_answer = input("Aapka jawab: ").strip().lower()
 
    if user_answer == answer.lower():
     print("Sahi!\n")
     score += 1
    else:
     print(f"Galat. Sahi jawab hai: {answer}\n")
 
 end_time = time.time()
 total_time = round(end_time - start_time, 2)
 
 print("-" * 30)
 print(f"Game over! Aapka final score hai: {score}/{len(quiz_data)}")
 print(f"Total time taken: {total_time} seconds")
 print("-" * 30)

if __name__ == "__main__":
 run_quiz()