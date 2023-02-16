<a name="readme-top"></a>

# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
- [💻 Getting Started](#getting-started)
  - [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
- [👥 Authors](#authors)
- [🤝 Contributing](#contributing)
- [⭐️ Show your support](#support)
- [🙏 Acknowledgements](#acknowledgements)
- [📝 License](#license)

<!-- PROJECT DESCRIPTION -->

# 📖 [A DISTRIBUTED SYSTEM] <a name="about-project"></a>

> Build a TCP server that can accept and hold a maximum of N clients (where N is configurable).These clients are assigned ranks based on first-come-first-serve, i.e whoever connects first receives the next available high rank. Ranks are from 0–N, 0 being the highest rank.

> Clients can send to the server commands that the server distributes among the clients. Only a client with a lower rank can execute a command of a higher rank client. Higher rank clients cannot execute commands by lower rank clients, so these commands are rejected. The command execution can be as simple as the client printing to console that command has been executed.

> If a client disconnects the server should re-adjust the ranks and promote any client that needs to be promoted not to leave any gaps in the ranks.

**[A DISTRIBUTED SYSTEM]** is a type of system that lets computers independent of each other work together.

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

> The project is built entirely using python

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://python.org/">Python</a></li>
  </ul>
</details>

<!-- Features -->

### Key Features <a name="key-features"></a>

> Describe between 1-3 key features of the application.

- **[Server to hold a maximum number of clients]**
- **[SErver distributing commands to clients]**
- **[The server can reassign a number to a client in the server queue]**

<p align="left">(<a href="#readme-top">back to top</a>)</p>

<p align="left">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>

> To get started with the project, make sure you have installed the following in your computer operating system

### Prerequisites

In order to run this project you need:

```sh
 Install python in your machine if you don't have
```

### Setup

Clone this repository to your desired folder:

```sh
 git clone https://github.com/paulmunyao/-A-distributed-system.git
```

### To run the project, execute the following command:

```sh
 python3 socketserver.py -- this is for running the socket side
 python3 clientserver.py -- this is for running the client side
```

<p align="left">(<a href="#readme-top">back to top</a>)</p>

<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

> Mention all of the collaborators of this project.

👤 **Author1**

- GitHub: [@githubhandle](https://github.com/paulmunyao)
- Twitter: [@twitterhandle](https://twitter.com/Mutiso_P)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/paul-munyao-869a8a165/)

<p align="left">(<a href="#readme-top">back to top</a>)</p>

<p align="left">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

> I would like to thank 

- https://github.com/EdwinWalela

- https://github.com/habbes

<p align="left">(<a href="#readme-top">back to top</a>)</p>

<p align="left">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="left">(<a href="#readme-top">back to top</a>)</p>
