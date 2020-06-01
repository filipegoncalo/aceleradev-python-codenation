# refatore o código melhorando a segurança, padrões e boas práticas.
from abc import ABC, abstractmethod

# Implemente o método `get_department` que retorna o nome do departamento e 
#   `set_department` que muda o nome do departamento para as classes 
#   `Manager` e `Seller`
class Department:
    def __init__(self, name, code):
        self.__department_name = name
        self.__department_code = code

    def get_department(self):
        return self.__department_name

    def set_department(self, new_name):
        self.__department_name = new_name   

# Proteja a classe `Employee` para não ser instânciada diretamente.
# Torne obrigatório a implementação dos métodos da classe `Employee`, 
#   implemente-os se for necessários.

# Padronize uma carga horária de 8 horas para todos os funcionários.
class Employee(ABC):
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary
        self.hours = 8
    
    def get_hours(self):
        return self.hours
    
    @abstractmethod
    def calc_bonus(self):
        pass

# Proteja o atributo `department` da classe `Manager` para que seja 
#   acessado somente através do método `get_department`.
class Manager(Employee, Department):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        super(Employee, self).__init__('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

# Proteja o atributo `sales` da classe `Seller` para que não seja acessado 
#   diretamente, crie um método chamado `get_sales` para retornar o valor do 
#   atributo e `put_sales` para acrescentar valores a esse atributo, 
#   lembrando que as vendas são acumulativas

# O cálculo do metodo `calc_bonus` do Vendedor dever ser calculado pelo 
#   total de suas vendas vezes 0.15
class Seller(Employee, Department):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        super(Employee, self).__init__('sellers', 2)
        self.__sales = 0

    def get_sales(self):
        return self.__sales

    def put_sales(self, sale):
        self.__sales += sale

    def calc_bonus(self):
        return self.__sales * 0.15