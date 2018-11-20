# encoding: utf-8
import rsa


class RSA(object):
    def create_keys(self):
        (public, private) = rsa.newkeys(int(2048))
        
        # Creating a public key
        public_key = 'public_key.txt'
        #Format public key to .PEM
        with open(public_key,'w') as file:
            file.write(public.save_pkcs1(format='PEM'))
            file.close()

        # Creating a private key
        private_key = 'private_key.txt' 
        with open(private_key,'w') as file:
            file.write(private.save_pkcs1(format='PEM'))
            file.close()

        print ('Public key created: {}'.format(public_key))
        print ('Private key created: {}\n'.format(private_key))

    def decrypt(self):
        private_key_file = 'private_key.txt'
        encrypted_message = 'encrypted.txt'

        key = ''
        with open(private_key_file, 'r') as file:
            for line in file:
                key += line

        private_key = rsa.PrivateKey.load_pkcs1(key, format='PEM')

        message_to_decrypt = ''
        with open(encrypted_message,'r') as file:
            for line in file:
                message_to_decrypt += line

        decrypted_message = rsa.decrypt(message_to_decrypt, private_key)
        
        print 'Message: {} \n'.format(decrypted_message)

    def encrypt(self):
        public_key_file = 'public_key.txt'
        message = raw_input('Type your message to encrypt: ')

        key = ''
        with open(public_key_file,'r') as file:
            for line in file:
                key += line

        public_key = rsa.PublicKey.load_pkcs1(key, format='PEM')

        encrypt_message = rsa.encrypt(message, public_key)

        encrypted_file = 'encrypted.txt'
        with open(encrypted_file, 'w') as file:
            file.write(encrypt_message)

        print 'Message encrypted in file {} \n'.format(encrypted_file)


if __name__ == '__main__':
    RSA()