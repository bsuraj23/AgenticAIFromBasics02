# AgenticAIFromBasics02



**task on (09-09-25):**
print(dir(x))       # shows methods of int object
print(dir(hello))   # shows attributes of function object
**Class Method**
Defined with @classmethod.
First argument is cls → refers to the class itself.
Can access or modify class-level data (shared across all objects).
Useful for alternative constructors or operations that affect the class as a whole.

**Task(10-09-25):**
to find all global variables:global().keys()
to find all class variables:class_name.__dict__.keys()
to find all instance variables:obj.__dict__.keys()
to find all local variables:local().keys()

**Task(15-09-25):**
import socket
compip=socket.gethostbyname(socket.gethostname())
print("the ip adress of this computer:",compip)   #returns :172.18.112.1

#here it connects with a host and transfers '0' data and verifies the ip4 adress
**def get_local_ip():**
    try:
       Connect to a remote host; no data is actually sent
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))  # Google's DNS
            return s.getsockname()[0]
    except Exception:
        return "Unable to determine IP"

if __name__ == "__main__":
    print("Local IP address:", get_local_ip())

**what thigs you need to take care to host a website**
Domain and DNS: register domain, configure A/AAAA records, TTLs
Hosting environment: choose between shared/VPS/dedicated/cloud
Web server software: Nginx, Apache, or Caddy
Application stack: language/runtime, frameworks, dependencies, containers
Security: TLS/HTTPS, patching, firewall, secure SSH
Performance and reliability: load balancing, caching, backups
Monitoring and logging: uptime metrics, logs, alerts
Compliance and privacy: data retention, GDPR/CCPA, policies
Maintenance: CI/CD, deployment pipelines, rollback plans
Legal/terms: TOS, licenses for used software

**library:**
A collection of functions/classes you call from your code.we can decide when to use library features.
Example: NumPy, Requests, Pandas.
you call the functions you need.
**framework**:A reusable, opinionated structure that calls your code (inversion of control).
Governs application architecture and lifecycle; you plug in components.
the framework calls your code at defined hooks and stages.
Examples: Django (Python web framework)

**what are the features of the website:**
Content presentation: text, images, video, responsive layout
Navigation: menus, breadcrumbs, internal linking
Interactivity: forms, validation, dynamic UI
Accessibility: screen-reader support, keyboard navigation
Performance: fast load times, asset optimization, caching
SEO: semantic HTML, metadata, sitemaps
Security: HTTPS, input validation, authentication
Reliability/compatibility: cross-browser consistency
Analytics/monitoring: user behavior data, error reporting
Backend integration: APIs, databases, auth services
Compliance: privacy policy, cookies, data protection

**task (16-09-25)**
-->Fast API:
API-first projects or microservices: If your primary deliverable is a fast, well-documented API (REST or GraphQL), FastAPI shines.
Performance requirements: FastAPI is built on ASGI (async) and tends to be faster than many traditional frameworks for I/O-bound workloads.

-->When to use Django:
Full-featured web applications: If you’re building a traditional server-rendered site with complex templates, authentication, admin interface, forms, and ORM‑driven data models, Django’s batteries-included approach is powerful.
Rapid CRUD apps with admin tooling: Django’s admin site is a strong productivity booster for content-heavy apps or internal tools.

-->Choose between them:
You’re building an API-only service with high performance needs? Lean toward FastAPI.
You’re building a traditional web app with admin UI, forms, and server-rendered pages? Django is often the first choice.

-->GDPR stands for General Data Protection Regulation. It’s the European Union’s data privacy and security regulation, in effect since May 25, 2018, with extra-territorial reach
Strengthen individuals’ data rights and give people more control over how their personal data is collected, stored, processed, and shared.
