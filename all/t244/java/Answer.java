package org.real.temp;

import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Answer {

    /**
     * Checks that the arguments passed to a given method object comply with their expected types,
     * based on the method's signature. If there's a discrepancy, it throws an IllegalArgumentException.
     *
     * @param methodObj The method for which arguments are checked.
     * @param args      Positional arguments passed to the method.
     * @param kwargs    Keyword arguments passed to the method.
     * @param exclude   Names of parameters to exclude from the type check.
     */
    public static void methodArgTypeCheck(Method methodObj, Object[] args, Map<String, Object> kwargs, List<String> exclude) {
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

    private static Map<String, Class<?>> getParameterTypes(Method method) {
        Map<String, Class<?>> parameterTypes = new HashMap<>();
        for (int i = 0; i < method.getParameterCount(); i++) {
            parameterTypes.put("arg" + i, method.getParameterTypes()[i]);
        }
        return parameterTypes;
    }

    private static Map<String, Object> combineArgs(Object[] args, Map<String, Object> kwargs) {
        Map<String, Object> combinedArgs = new HashMap<>(kwargs);
        for (int i = 0; i < args.length; i++) {
            combinedArgs.put("arg" + i, args[i]);
        }
        return combinedArgs;
    }

    public static void main(String[] args) {
        try {
            Method method = Answer.class.getMethod("exampleMethod", int.class, String.class);
            Map<String, Object> kwargs = new HashMap<>();
            kwargs.put("b", "hello");
            methodArgTypeCheck(method, new Object[]{123}, kwargs, null);
            System.out.println("Arguments are valid.");
        } catch (NoSuchMethodException | IllegalArgumentException e) {
            e.printStackTrace();
        }
    }

    public static void exampleMethod(int a, String b) {
        // Example method body
    }
}