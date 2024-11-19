[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-support%20my%20work-FFDD00?style=flat&labelColor=101010&logo=buy-me-a-coffee&logoColor=white)](https://www.buymeacoffee.com/r0mymendez)

---

# ⚙️ Doc as Code Tutorial

## 🚀 Docusaurus  
**Docusaurus** is an excellent solution for implementing a documentation portal that can be `easily updated with code`, helping to keep your software development project documentation up-to-date and versioned.  

In this repository, I have created a simple site to document the data model and machine learning project.  

The documentation will include `charts`, `tables`, and `architecture` examples, providing a comprehensive and `easy-to-understand` guide on how to implement this framework in combination with two other **🐍Python** libraries.

## What is Documentation as Code?  
Documentation and its updates are an important process in many companies that develop software, where this process is carried out using different tools, many of which are paid solutions.  
Therefore, in recent times, the concept of **"doc as code"** has emerged. This means using the same tools and workflow used in software development to `manage`, `version`, and `deploy` documentation.  
This approach not only allows for better tracking of the documentation but also facilitates its maintenance and ensures alignment with the same best practices used in software development, not just in the code but also in the documentation.

![img-preview](img/preview.png)


---

# Practices and Benefits of Documentation as Code

## Tools and Practices for Documentation as Code

For the development of these sites, it is essential to understand some practices and tools that allow us to implement this approach. Below is a detailed list of the most important aspects to cover in this tutorial.

- 📝 **Markdown**: It is the most common markup language for writing documentation due to its simplicity and ability to integrate with version control platforms and static site generators.
- 🗂️ **Git**: Git allows versioning documentation just like code. Thanks to Git, each change in the documentation is recorded, enabling teams to track edits, revert changes, and collaborate more efficiently.
- 🔄 **Gitflow**: This methodology provides a structured workflow to manage versions and revisions of documentation, ensuring that any change is approved and tested before reaching production. Gitflow also facilitates collaboration between teams, allowing for safe and organized change management.
- ☁️ **Cloud Services**: By using services like AWS S3, Netlify, or GitHub Pages, you can deploy documentation at a low cost. These services allow you to create static sites, which are fast, secure, and easily accessible to users.
- 🌐 **Static Site Generators**: Tools like Docusaurus, Jekyll, or Hugo take documentation written in Markdown and convert it into a navigable website. This allows you to create rich and organized documentation without the need for a server.
- 🚀 **Continuous Integration (CI/CD)**: Using CI/CD pipelines (such as GitHub Actions, GitLab CI, or Jenkins) allows you to automatically deploy changes to the documentation when a new version is merged or modifications are approved. This ensures that the documentation is always up-to-date and available.

![img-tools](img/tools_practices.png)


---

# 🦖 Docusaurus Overview  

**Docusaurus** is an open-source project developed by Meta in 2007 that simplifies the creation, deployment, and maintenance of documentation websites in a fast and efficient way. It allows the use of Markdown and MDX to write content, while its core built on React enables full customization of the styles to fit the specific needs of the project.

Additionally, Docusaurus supports Mermaid through the `@docusaurus/theme-mermaid` plugin, enabling the inclusion of charts and diagrams directly within the documentation.

---

## Mermaid  
Mermaid is a **JavaScript** library for creating diagrams and charts from text. By integrating with MkDocs Material, Mermaid allows you to generate visualizations such as flowcharts, entity-relationship diagrams, and other charts within the documentation without the need for external tools.

![img-preview](img/mermaid.png)

---

## 🧩 Dynamic Page: Jinja2  
**Jinja2** is a library that allows embedding variables and data from Python dictionaries into HTML, making web pages dynamic. This library is commonly used for generating dynamic HTML and sending personalized emails.

---


# 📝 Tutorial: Building a Documentation Site for a Machine Learning Pipeline  

Now that I’ve covered the theory behind **Documentation as Code** along with key practices and tools, it’s time to dive into the hands-on part of this tutorial. In this section, I’ll guide you through how I created a documentation site for a small machine learning pipeline solution using synthetic health data from a medical entity.  

### 📚 Structure of the Site  
The site I’ve built includes the following pages:  

* 📄 **Introduction**: The home page with an overview of the project.  
* 📄 **Tables**: An explanation of Synthea-generated data tables.  
* 📄 **Architecture**: A description of the data processing architecture in AWS.  
* 📄 **Glossary**: A glossary of key terms and concepts.  

### 🛠️ Dynamic Content with Jinja2  

To make the documentation dynamic, I’ve leveraged **Jinja2**. This allowed me to include real-time and automated data updates throughout the site:  

* **Introduction Page**: I’ve added functionality to display the date of the last documentation update, which is dynamically retrieved from a database table.  
* **Tables Page**: I used Jinja2 to showcase a data table by dynamically rendering the first few rows of a dataframe query.  
* * The **architecture** page explains the architecture supporting this functionality, and further details can be found in another repository called [diagram-as-code](https://github.com/r0mymendez/diagram-as-code), which provides the blueprint for implementation.  


![Documentation Site Preview](img/docusaurus_build-serve.png)
