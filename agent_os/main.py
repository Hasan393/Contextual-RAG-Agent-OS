import os
import google.generativeai as genai
from dotenv import load_dotenv
from kernel.memory_hierarchy import MemoryHierarchy
from kernel.attention_controller import compress_memory
from kernel.knowledge_graph import KnowledgeGraph
from kernel.retrieval_optimizer import RetrievalOptimizer

def main():
    load_dotenv()
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    memory = MemoryHierarchy()
    kg = KnowledgeGraph()
    optimizer = RetrievalOptimizer()

    print("==================================================")
    print(" 🧠 Contextual-RAG-Agent-OS Boot Sequence Initiated ")
    print("==================================================")

    while True:
        user_input = input("\nUser: ")
        if user_input.lower() in['exit', 'quit']:
            break

        memory.add_short_term(f"User: {user_input}")
        
        kg.extract_and_update(model, user_input)
        
        system_context = f"""
        [SYSTEM MEMORY STATES]
        Optimization Weight: {optimizer.strategy_weight}
        Long Term Memories: {memory.long_term}
        Knowledge Graph: {kg.graph}
        Recent Buffer: {memory.short_term}
        """
        
        prompt = f"System Context:\n{system_context}\n\nRespond directly to the user's latest message."
        response = model.generate_content(prompt)
        bot_reply = response.text.strip()
        
        print(f"OS-Agent: {bot_reply}")
        memory.add_short_term(f"OS-Agent: {bot_reply}")
        
        compression_result = compress_memory(model, memory)
        if compression_result:
            print(f"\n[SYSTEM ALERT: Short-term buffer capacity reached.]")
            print(f"[SYSTEM ALERT: Executing Memory Compression...]")
            print(f"[COMPRESSED KERNEL]: {compression_result}")
            
            optimizer.optimize(1.0)

if __name__ == "__main__":
    main()