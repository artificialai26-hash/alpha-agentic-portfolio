import os
import json
import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader

def load_projects():
    projects_dir = os.path.join("content", "projects")
    projects = []
    
    for filename in sorted(os.listdir(projects_dir)):
        if filename.endswith(".md"):
            filepath = os.path.join(projects_dir, filename)
            post = frontmatter.load(filepath)
            
            # Convert body markdown to HTML
            html_content = markdown.markdown(post.content)
            
            projects.append({
                "index": post.get("index", "00"),
                "status": post.get("status", "active"),
                "name": post.get("name", "unnamed-project"),
                "problem": post.get("problem", ""),
                "approach": post.get("approach", ""),
                "result": post.get("result", ""),
                "tags": post.get("tags", []),
                "github": post.get("github", "#"),
                "content": html_content
            })
    return projects

def load_training_log():
    log_path = os.path.join("content", "training_log.json")
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            return json.load(f)
    return []

def render_site():
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("index.html")
    
    projects = load_projects()
    training_log = load_training_log()
    
    output_html = template.render(
        projects=projects,
        training_log=training_log
    )
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(output_html)
        
    print("[SUCCESS] Site compiled successfully to index.html")

if __name__ == "__main__":
    render_site()