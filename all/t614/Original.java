//Everything beyond this point was written by ChatGPT im not that smart
    public static Map<HatType, Double> getDiffOfAvgHeightDiffsToPredecessorByHatType(List<Adventuin> adventuins) {
        Map<HatType, Double> result = new HashMap<>();

        Map<HatType, List<Adventuin>> groupedByHatType = groupByHatType(adventuins);

        for (Map.Entry<HatType, List<Adventuin>> entry : groupedByHatType.entrySet()) {
            HatType hatType = entry.getKey();
            List<Adventuin> hatTypeAdventuins = entry.getValue();

            Map<Integer, List<Integer>> differencesBySign = calculateDifferencesBySign(hatTypeAdventuins);

            // Calculate average differences for each sign category
            double avgNegative = calculateAverage(differencesBySign.getOrDefault(-1, new ArrayList<>()));
            double avgZero = calculateAverage(differencesBySign.getOrDefault(0, new ArrayList<>()));
            double avgPositive = calculateAverage(differencesBySign.getOrDefault(1, new ArrayList<>()));

            // Calculate the absolute difference between averages
            double absDiff = Math.abs(avgNegative - avgPositive);
            result.put(hatType, absDiff);
        }

        return result;
    }
