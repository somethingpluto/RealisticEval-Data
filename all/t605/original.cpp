//Written with ChatGPT
#include <iostream>
#include <string>

class Usuario {
private:
    std::string nombre;
    double peso;
    double altura;

public:
    // Default constructor
    Usuario() {}

    // Parameterized constructor
    Usuario(const std::string& nombre, double peso, double altura)
        : nombre(nombre), peso(peso), altura(altura) {}

    // Setter and Getter for nombre
    void setNombre(const std::string& nombre) { this->nombre = nombre; }
    std::string getNombre() const { return nombre; }

    // Setter and Getter for peso
    void setPeso(double peso) { this->peso = peso; }
    double getPeso() const { return peso; }

    // Setter and Getter for altura
    void setAltura(double altura) { this->altura = altura; }
    double getAltura() const { return altura; }

    // Calculate BMI
    double calcularBMI() const {
        if (altura <= 0.0) {
            std::cout << "Error: Altura inválida" << std::endl;
            return 0.0;
        }

        double alturaMetros = altura / 100.0;  // Convert altura from cm to meters
        return peso / (alturaMetros * alturaMetros);
    }

    // Print nombre
    void printNombre() const {
        std::cout << "Nombre: " << nombre << std::endl;
    }

    // Overloading the << operator
    friend std::ostream& operator<<(std::ostream& out, const Usuario& usuario) {
        out << "Nombre: " << usuario.nombre << std::endl;
        out << "Peso: " << usuario.peso << std::endl;
        out << "Altura: " << usuario.altura << std::endl;
        return out;
    }
};