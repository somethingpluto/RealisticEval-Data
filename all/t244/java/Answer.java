package org.real.temp;

import java.lang.reflect.Method;
import java.util.Arrays;
import java.util.List;

public class Answer {

    public static void methodArgTypeCheck(Method methodObj, Object... args) throws Exception {
        Class<?>[] parameterTypes = methodObj.getParameterTypes();

        if(parameterTypes.length != args.length){
            throw new IllegalArgumentException("Number of arguments do not match");
        }

        for(int i=0; i<parameterTypes.length; i++){
            if(!parameterTypes[i].isInstance(args[i])){
                throw new IllegalArgumentException("Argument " + i + " is of wrong type");
            }
        }
    }

    // Example usage:
    public static void main(String[] args) throws Exception {
        Method method = Answer.class.getMethod("exampleMethod", String.class, int.class);
        methodArgTypeCheck(method, "Hello", 123); // Correct

        try{
            methodArgTypeCheck(method, "Hello", "World"); // Incorrect
        } catch(IllegalArgumentException e){
            System.out.println(e.getMessage());
        }
    }

    private static void exampleMethod(String str, int num) {
        // Do something...
    }
}