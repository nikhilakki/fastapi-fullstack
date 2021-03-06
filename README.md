<!--
 Copyright (c) 2021 Nikhil Akki
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->
# FastAPI Full Stack Boilerplate ๐ฝ๏ธ

An opinionated yet highly customizable FastAPI implementation with best practices, Django Admin inspired - user & group module, Docker and more.

*The current build is not functional yet. However, this project is under active development, and we anticipate the first beta should be out by Q4, 2021.*


## Features & Roadmap - โณ

**Backend** - ๐ญ
- [X] Base structure ๐๏ธ
- [ ] JWT Authentication ๐
- [ ] Django Admin like features -
  - [ ] User module ๐
  - [ ] Group module ๐จโ๐จโ๐งโ๐ฆ
  - [ ] Permissions module ๐ช
- [X] Packaging ๐
  - [X] Docker support ๐ข
  - [x] Pipenv support ๐ผ
- [ ] Testing ๐งช
  - [ ] Unit tests with pytest ๐ฉบ
- [ ] Fully Async ๐
- [ ] Celery integration ๐ท

**Database for Admin UI** - ๐
- [ ] SQL (using SQLAlchemy) โ๏ธ
  - [x] SQLite3 (local dev & testing)
  - [ ] PostgreSQL (prod and dockerised env)
  
> *You can use any kind of db for the APIs you build*

**Frontend** - ๐ป
- [ ] React based Admin UI
  - [ ] Login page
  - [ ] Admin dashboard
    - [ ] List view for User & Group table
    - [ ] List view for custom components
    - [ ] Create new record
- [ ] Packaging
  - [ ] Docker support ๐ข

**Tooling** - ๐งฐ
- [ ] CLI tool
  - [ ] Custom project skafolding
  - [ ] Generate component boilerplate
  - [ ] Ability to choose components like Admin UI, Deployment recipes etc.

**Deploymeny Receipes** - ๐ฅ
- [ ] Docker compose (Single node deployment)
- [ ] Kubernetes (Production deployment)

**Platform Receipes**
- [ ] Terraform (Infra provisioning)
  - [ ] GCP GKE
  - [ ] AWS EKS
  - [ ] Digital Ocean K8s Cluster

### Todos (readme & repo) -
- [ ] Installation & Quick Start
- [ ] Wiki page
- [ ] API Documentation on Github pages
- [ ] Contribution Guide for developers

> - Author - [Nikhil Akki](http://nikhilakki.in) ๐
> - Version - 0.1.0-alpha
> - License - MIT ๐ค

*This project won't be possible without the amazing work of awesome developers of various projects on the shoulders this one stands.* ๐
