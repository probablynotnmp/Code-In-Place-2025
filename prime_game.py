import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    print("🎯 PRIME NUMBER GUESSING GAME 🎯")
    print("I'm thinking of a prime number between 1 and 100!")
    print("Can you guess it?\n")
    
    # Generate a random prime number between 1 and 100
    primes = [n for n in range(2, 101) if is_prime(n)]
    secret_prime = random.choice(primes)
    
    guesses = 0
    max_guesses = 7
    
    while guesses < max_guesses:
        try:
            guess = int(input(f"Guess #{guesses + 1}: "))
            guesses += 1
            
            if guess == secret_prime:
                print(f"🎉 YES! {secret_prime} is correct!")
                print(f"You got it in {guesses} guesses!")
                break
            elif not is_prime(guess):
                print(f"❌ {guess} is not even a prime number!")
            elif guess < secret_prime:
                print(f"📈 {guess} is prime, but too low!")
            else:
                print(f"📉 {guess} is prime, but too high!")
                
            if guesses < max_guesses:
                print(f"You have {max_guesses - guesses} guesses left.\n")
                
        except ValueError:
            print("Please enter a valid number!")
            guesses -= 1  # Don't count invalid input as a guess
    
    if guesses == max_guesses and guess != secret_prime:
        print(f"💀 Game Over! The number was {secret_prime}")
    
    print(f"\n🧠 Fun fact: There are {len(primes)} prime numbers between 1 and 100!")
    
    # Ask if they want to play again
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again == 'y' or play_again == 'yes':
        print("\n" + "="*50 + "\n")
        main()
    else:
        print("Thanks for playing! 🎮")

if __name__ == "__main__":
    main()