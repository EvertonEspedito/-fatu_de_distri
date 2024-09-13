def main():
    # Solicita a entrada do usuário
    string_original = input("Digite a string para inverter: ")
    
    # Inverte a string
    string_invertida = inverter_string(string_original)
    
    # Exibe o resultado
    print(f"String original: {string_original}")
    print(f"String invertida: {string_invertida}")

if __name__ == "__main__":
    main()
