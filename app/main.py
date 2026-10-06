from app.rag_pipeline import run_rag

query = input("Customer:")

answer = run_rag(query)

print("\n==== FINAL ANSWER ====")
print(answer)

