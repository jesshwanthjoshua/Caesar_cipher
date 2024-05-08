alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# print(f"len(alphabet) = {len(alphabet)}")

from art import logo
print(logo)
game = True

def ceaser(direction,text,shift):
  message = ""

  for x in text:
    if x not in alphabet:
      message += x
      
    else:  
      position = int(alphabet.index(x))
      
      if direction == "encode":        
        shift_size = position + shift
        if shift_size >= len(alphabet):
          shift_size = abs(len(alphabet) - shift_size)
    
      elif direction == "decode":
        shift_size = position - shift
        
      message += alphabet[shift_size]
      
  if direction == "encode":
    print(f"Encrypted message: {message}.")
    
  elif direction == "decode":
    print(f"Decrypted message: {message}.")

while game == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  ceaser(direction,text,shift)
  
  choice = input("Type 'Y' to continue the Ceaser Cipher program or 'N' to end: ").lower()
  if choice == 'n':
    game = False
