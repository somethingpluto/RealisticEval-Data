package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

import java.lang.reflect.Method;
import java.util.HashMap;
import java.util.Map;

/**
 * Test class for method argument type checking.
 */
public class Tester {

    @Test
    public void testCorrectTypes() {
        /**
         * Test with correct argument types.
         */
        try {
            Method method = MyClass.class.getMethod("myMethod", int.class, String.class, float.class);
            MyClass instance = new MyClass();
            methodArgTypeCheck(method, new Object[]{instance, 10, "hello", 3.14f}, new HashMap<>(), null);
        } catch (NoSuchMethodException | IllegalArgumentException e) {
            fail("methodArgTypeCheck() raised an exception unexpectedly!");
        }
    }

    @Test(expected = IllegalArgumentException.class)
    public void testMissingArgument() {
        /**
         * Test with missing required argument.
         */
        Method method = MyClass.class.getMethod("myMethod", int.class, String.class, float.class);
        MyClass instance = new MyClass();
        methodArgTypeCheck(method, new Object[]{instance, 10}, new HashMap<>(), null);
    }

    // Utility method for type checking
    private void methodArgTypeCheck(Method methodObj, Object[] args, Map<String, Object> kwargs, List<String> exclude) {
        if (exclude == null) {
            exclude = new ArrayList<>();
        }
        exclude.add("self");  // Exclude 'self' by default since it refers to the method's instance

        Map<String, Class<?>> parameterTypes = getParameterTypes(methodObj);
        Map<String, Object> combinedArgs = combineArgs(args, kwargs);

        for (Map.Entry<String, Class<?>> entry : parameterTypes.entrySet()) {
            String paramName = entry.getKey();
            Class<?> expectedType = entry.getValue();

            if (!exclude.contains(paramName) && combinedArgs.containsKey(paramName)) {
                Object actualValue = combinedArgs.get(paramName);
                if (!expectedType.isInstance(actualValue)) {
                    String passedArgType = actualValue.getClass().getSimpleName();
                    String expectedArgType = expectedType.getSimpleName();
                    throw new IllegalArgumentException(
                            String.format("%s should be of type %s, but got type %s instead.",
                                    paramName, expectedArgType, passedArgType));
                }
            }
        }
    }

    private Map<String, Class<?>> getParameterTypes(Method method) {
        Map<String, Class<?>> parameterTypes = new HashMap<>();
        for (int i = 0; i < method.getParameterCount(); i++) {
            parameterTypes.put("arg" + i, method.getParameterTypes()[i]);
        }
        return parameterTypes;
    }

    private Map<String, Object> combineArgs(Object[] args, Map<String, Object> kwargs) {
        Map<String, Object> combinedArgs = new HashMap<>(kwargs);
        for (int i = 0; i < args.length; i++) {
            combinedArgs.put("arg" + i, args[i]);
        }
        return combinedArgs;
    }

    // Example method to demonstrate usage
    public static class MyClass {
        public void myMethod(int arg1, String arg2, float optionalArg) {
            // Method body
        }
    }
}