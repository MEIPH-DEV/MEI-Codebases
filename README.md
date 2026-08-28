# MedEthix Technical Ecosystem — Transferred Codebases Directory

This repository/directory serves as the master index and operational guide for all **14 application codebases** transferred from the legacy hosting infrastructure (`servers.mackydaus.com`) into the official **MedEthix Inc. (MEI) Technical Ecosystem** as part of **Server Migration Phase 1 & Phase 2** (Ref: `MEI-POL-2026-011` & `MEI-POL-2026-012`).

---

## 📌 Important Architectural Boundary Disclaimer
> **CRITICAL:** While these 14 codebases and their associated operational databases support live e-commerce transactions, inventory display, and therapeutic web portals across MEI & CHW brand properties, **they are strictly independent and NOT part of the MeiMei AI Engine core database, primary vector indexes, or knowledgebases**. 
>
> All **MeiMei AI Engine** intelligence repositories, inference pipelines, and RAG (Retrieval-Augmented Generation) vector stores reside in dedicated, isolated infrastructure environments.

---

## 📂 Transferred Codebases Inventory

Below is the verified registry of all 14 transferred codebases, organized by therapeutic and operational domain, along with their official GitHub Enterprise repository mappings:

### 1. Pediatric & Specialized Care
* **Pedia Codebases** (`mei-org/pedia-app`): Pediatric product catalog, dosing charts, and specialized web interfaces.
* **Medifilm D3 Codebases** (`mei-org/medifilm-d3`): Medifilm D3 brand page, product formulation logic, and SKU specifications.
* **Mitubaby Codebases** (`mei-org/mitubaby-app`): Mitubaby product lines, e-commerce assets, and promotional modules.
* **NYU Codebases** (`mei-org/nyu-app`): Specialized clinical application modules and institutional portal interfaces.
* **Medifilm Zimelt Codebases** (`mei-org/medifilm-zimelt`): Medifilm Zimelt product listing, consumer guides, and checkout pipelines.

### 2. Fast Aid Product Line
* **Fast Aid Mist-Dress Codebase** (`mei-org/fastaid-mistdress`): Specialized landing environment and application guidelines for Fast Aid Mist-Dress.
* **Fast Aid Relispray Codebase** (`mei-org/fastaid-relispray`): Fast Aid Relispray product showcase, distribution logic, and campaign pages.
* **Fast Aid Vinodine Codebase** (`mei-org/fastaid-vinodine`): Fast Aid Vinodine e-commerce catalog display and transactional endpoints.
* **Fast Aid General Codebase** (`mei-org/fastaid-general`): Central Fast Aid brand hub, master product indexes, and promo mechanics.

### 3. Corporate & Institutional Frameworks
* **MedEthix General** (`mei-org/medethix-core`): Central corporate portal, global navigation components, root API routing, and security profiles.
* **Godrej General** (`mei-org/godrej-ph-core`): Godrej Philippines official web environment, localized content management, and brand assets.

### 4. Medical Specialties & Therapeutics
* **Urology Codebase** (`mei-org/urology-med`): Specialized urology therapeutic catalog and practitioner portal routes.
* **Gen OB Codebase** (`mei-org/gen-ob-med`): General Obstetrics product pages, medical resources, and web applications.
* **RM (Reproductive Medicine) Codebase** (`mei-org/rm-med`): Reproductive Medicine specialty catalog and information modules.

---

## 🛠️ Repository Governance & Deployment Workflow

### 1. Version Control & Access Control
* **Organization:** All repositories are hosted under the official `mei-org` GitHub Enterprise organization.
* **Authentication:** Access requires mandatory **Multi-Factor Authentication (MFA)** with role-based access permissions.
* **Branch Protection Rules:** The `main` and `production` branches are protected. Pushing directly to production branches is disabled.

### 2. Dual-Custody Approval Matrix
In accordance with joint governance policies (`MEI-POL-2026-004`):
* Any Pull Request (PR) merged into `main` or `production` across these 14 codebases requires **at least two (2) approvals**:
  1. **MEI IT Approval:** John Balnig (*MEI IT Supervisor*) or designated IT System Lead.
  2. **CHW Digital Approval:** Macky Daus (*Digital Marketing Manager*) or designated Digital Lead.

### 3. Continuous Integration & Deployment (CI/CD)
* Automated deployment runners deploy staging builds upon opening a PR.
* Production deployments require dual approval sign-off in GitHub Actions before executing target server deployment scripts.

---

## 📋 Audit & Verification Compliance

| Audit Milestone | Status | Policy Ref | Key Signatories |
| :--- | :---: | :---: | :--- |
| **Phase 1: Codebase Transfer** | ✅ Completed | `MEI-POL-2026-011` | John Balnig (IT) / Macky Daus (Digital) |
| **Phase 2: Database Migration & GitHub Onboarding** | ✅ Completed | `MEI-POL-2026-012` | John Balnig (IT) / Macky Daus (Digital) |
| **Phase 3: DNS & Sites Transfer** | 🔄 Scheduled (Aug 24 – Sep 4) | `MEI-POL-2026-004` | Joint IT & Digital Teams |

---

## 📬 Support & Escalation Contacts

For technical issues, access requests, or pipeline failures, contact the joint management leads:

* **MEI IT Department:** John Balnig — *MEI IT Supervisor* (`john@medethix.com.ph`)
* **CHW Digital Team:** Macky Daus — *Digital Marketing Manager* (`digital@medethix.com.ph`)

---
*© 2026 MedEthix Inc. & CHW Digital Team. Confidential and Proprietary.*
