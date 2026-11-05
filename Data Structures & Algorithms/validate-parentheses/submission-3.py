class Solution:
    def isValid(self, s: str) -> bool:
        
        map = {
            '}':'{',
            ']':'[',
            ')':'(',
        }

        stack = []
        
        for i in s:
            # Si es llave cerrada
            if i in map:
                # Obtener par que abre
                pair = map[i]
                # Si la llave abierta esta en el stack
                if pair in stack:
                    # Si es la ultima
                    if (pair == stack[-1]):
                        # Eliminar (cerrar par)
                        stack.pop()
                    else: 
                        return False
                else:
                    return False
            # Si es llave abierta
            else:
                stack.append(i)
        
        if len(stack) == 0:
            return True
        else:
            return False


        
