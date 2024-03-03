# medical
### Well diversified Hospital Management System
---

> Linux Pre-requisites
>> $ ``` sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config libmysqlclient-dev default-libmysqlclient-dev mysqlclient ```

> Run XAMPP Control Panel
>> $ ```sudo /opt/lampp/manager-linux-x64.run```

> Python Pre-requisites
>> $ ```pip install -r requirements_python.txt```

> Pycharm Pre-requisites
>> Set **backend** as source root

> Docker Pre-requisites
> #### Add Docker's official GPG key:
> ```
>> sudo apt-get update
>> sudo apt-get install ca-certificates curl
>> sudo install -m 0755 -d /etc/apt/keyrings
>> sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
>> sudo chmod a+r /etc/apt/keyrings/docker.asc
> ```
> #### Add the repository to Apt sources:
> ```
>> echo \
>>   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
>>   $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
>>   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
>> sudo apt-get update
> ```
> #### install the latest version, run:
> ```
>> sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
>> sudo docker run hello-world
> ```

---
> External Api(s) and Tool(s) used:
> 
>> 1. <a href="https://freecurrencyapi.com/">Currency Conversion rate : FreeCurrencyAPI</a>
>> 2. <a href="https://chat.openai.com/">Code Documentation Generated using : Chat GPT</a>
---
> Git Flow:
>> ![medical-GIT FLOW.png](document%2Fmedical-GIT%20FLOW.png)
---
> ER Diagram:
>> ![medical-ER Diagram.png](document%2Fmedical-ER%20Diagram.png)
