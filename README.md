# Inus MemeBot
![Inus](img/inus.jpg)  
Discord Bot for the Inus online community    
Implements text responses  
Meme Responses(Searchs for a imagen when "#" leads the message sent)


## Dependencies
-[discord.py](https://discordpy.readthedocs.io/en/stable/)

## Host
Currently hosted in [AWS EC2](https://aws.amazon.com/ec2/) freetier 

## Files
- **img:** Folder contains imagen files 
    -- Image file format named as the call 
- **create_dic.py:** Creates a python dictonary with the imagen files 
- **dic.py:** Python dictonary with entrys for meme responses
- **main.py** Contains the Bot configuration and key
- **key.env** (Not included due security reasons) Contains the bot key generated at [Discord Applications](https://discord.com/developers/applications)

## Set Up
1. Git clone  
2. Follow steps to create a bot in [Discord Applications](https://discord.com/developers/applications)  
3. Open **create_dic.py** and edit the paths as needed   
4. Execute bash command in the folder "YourPath/MemeBot/"  
5. `python create_dic.py`  
6. Get the discord app key and create a key.env file with the key inside
7. `python main.py`

## Usage
The bot will response with a meme coresponding to the comand
`#memename`

