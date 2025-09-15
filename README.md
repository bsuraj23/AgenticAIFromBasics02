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

