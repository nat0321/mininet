# Installing Go on Linux
<br /><br />
Step 1:
<br />
Download go version 1.20.3 for Linux from the link: https://go.dev/dl/
<br /><br />
Step 2:
<br />
In the directory where the file was downloaded run the following commands:
<br />
`sudo rm -rf /usr/local/go`
<br />
`sudo tar -C /usr/local -xzf go1.20.3.linux-amd64.tar.gz`
<br /><br />
Step 3:
<br />
Add this line to the last line of the following files: `export PATH=$PATH:/usr/local/go/bin`
<br />
`sudo nano $HOME/.profile`
<br />
`sudo nano /etc/profile`
<br /><br />
Step 4:
<br />
Restart the VM or computer
<br /><br />
Step 5:
<br />
Check installation with: `go version`
