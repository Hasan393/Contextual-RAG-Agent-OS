import json

class KnowledgeGraph:
    def __init__(self):
        self.graph = {}

    def extract_and_update(self, model, text):
        prompt = f"Extract entities and relationships from this text as strict JSON format with keys 'entities' and 'relationships':\n{text}"
        try:
            response = model.generate_content(prompt)
            cleaned = response.text.replace("```json", "").replace("```", "").strip()
            data = json.loads(cleaned)
            
            for entity in data.get("entities",[]):
                if isinstance(entity, str) and entity not in self.graph:
                    self.graph[entity] =[]
                    
            for rel in data.get("relationships",[]):
                source = rel.get("source", "")
                target = rel.get("target", "")
                relation = rel.get("relation", "")
                if source in self.graph:
                    self.graph[source].append({target: relation})
        except:
            pass