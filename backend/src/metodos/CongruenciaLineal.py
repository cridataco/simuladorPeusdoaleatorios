class GeneratorNum:
    def __init__(self, a=5, xn=7, c=3, mod=16, iterations=20, min_val=4, max_val=19):
        self.a = a
        self.xn = xn
        self.c = c
        self.mod = mod
        self.iterations = iterations
        self.min_val = min_val
        self.max_val = max_val
        self.generated_numbers = []  # Lista para almacenar los números generados
    
    def generate_xi(self):
        return (self.a * self.xn + self.c) % self.mod
    
    def generate_ri(self):
        return self.xn / (self.mod - 1)
    
    def generate_ni(self):
        return self.min_val + (self.max_val - self.min_val) * self.generate_ri()
    
    def generate_all_numbers(self):
        result = ""
        self.generated_numbers.clear()  
        for i in range(self.iterations):
            self.xn = self.generate_xi()
            ri = self.generate_ri()
            ni = self.generate_ni()
            self.generated_numbers.append(ni)  
            result += f"{i} - Xi| {self.xn} - Ri| {ri:.4f} - Ni| {ni:.4f}\n"
        return result
    
    def get_generated_numbers(self):
        return self.generated_numbers 

# Ejemplo de uso
if __name__ == "__main__":
    gen = GeneratorNum()
    print(gen.generate_all_numbers())
    print("\nLista de números generados:", gen.get_generated_numbers())
