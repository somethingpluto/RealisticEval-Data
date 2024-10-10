package org.real.temp;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Answer {

    public static List<String[]> checkDividendVariances(List<String[]> records) {
        Map<String, Double> map = new HashMap<>();
        List<String[]> result = new ArrayList<>();

        for(String[] record : records){
            String ticker = record[0];
            String exDividendDate = record[1];
            double dividendAmount = Double.parseDouble(record[2]);

            if(map.containsKey(ticker + "-" + exDividendDate)){
                if(dividendAmount != map.get(ticker + "-" + exDividendDate)){
                    result.add(new String[]{ticker, exDividendDate});
                }
            } else {
                map.put(ticker + "-" + exDividendDate, dividendAmount);
            }
        }

        return result;
    }
}