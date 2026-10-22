# Automated DevSecOps Pipeline with Automated GitOps Feedback Loop

An enterprise-grade, fully automated DevSecOps CI/CD pipeline that shifts security left. Built with GitHub Actions, Trivy, Docker, and an automated GitOps delivery feedback loop to prevent insecure containerized applications from reaching production.

---

## 💟 System Architecture & Workflow

```text
                      +----------------------------
+
                      |  Developer Code Push       |
                       +------------+---------------+
                                   |
                                   v (GitHub Push Event)
          +-------------------------------------------------------+
          |            DEVSECOPS AUTOMATED GATEKEEPER            |
          |                                                       |
          |  1. Code Quality & Unit Tests (PyTest)"Ran 2 Tests OK"  |
          |                          |                             |
          |                          v                             |
          |  2. Secure Docker Build (Non-Root User + Slim Base)     |
          |                          |                             |
          |                         v                             |
          |  3. Aqua Trivy Container Vulnerability Audit            |
          |     (Severity: critical | Blocks on CVE Detection)      |
          {-------------------------+------------------------------}
               | (CVE Detected)        | (Zero Critical CVEs)
               v                       v
      + -------------- +        +-------------------------------+
      | Gatekeeper     |        | 4. GitOxs Delivery Feedback |
      | Blocks Build    |        |    Deployment Manifest Seal |
      | (Exit Code 1)   |        +--------------+---------------+
      + -------------- +                       |
                                                v
                                         +-----------------------------+
                                         | Kubernetes / ArgoCD Engine |
                                         | (Zero-Downtime Sync)      |
                                         +-----------------------------+
```

---

## 🚀 Key DevSecOps Features

- **Automated Unit Testing:** Unit tests verify application endpoints and liveness checks before container builds are triggered.
- **Security Shift-Left (Aqua Trivy):** Implemented automated security gates in the CI[0] stage, evaluating container dependencies and blocking builds if critical CVE breaches exist.
- **Least-Privilege Containerization:** Dockerfile is configured with dedicated non-root users (`appuser`), minimizing runtime exploitation risks.
- **GitOps Delivery Loop:** Passed commits automatically verify and signal deployment manifests for ArgoCD/serlf-healing reconciliation.

---

## 📸 Proof-of-Work & Verification Runs

### 1. End-to-End Passed Pipeline (Platform Success)
!All Jobs Passed(docs/screenshots/01-pipeline-success.png)

### 2. Security Gatekeeper Simulation (Failure Blocked)
!Security Blocked(docs/screenshots/02-security-blocked.png)

---

## 🛿 Tech Stack

- **CI/CD & Automation:** GitHub Actions
- **Security & SAST:** Aqua Trivy Scanner
- **Containerization:** Docker, Docker Buildx
- **Workload & Tests:** Python 3.11, PyTest, UnitTest
- **GitOps Manifests:** Kubernetes Deployments, ClusterIP Services

---

## 🔪 How to Run Locally


```bash
# 1. Run Unit Tests
$ python3 -m unittest discover -s tests

# 2. Build Docker Container
$ docker build -t secure-webapp:latest .

# 3. Run Container
$ docker run -d -p 8000:8000 secure-webapp:latest
```
