export function formatBytes(
    bytes: number,
    options?: {
      decimals?: number;
      sizeType?: "accurate" | "normal";
    }
): string;
