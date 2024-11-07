import { PI } from "mathjs";

function degreesToRadians(degrees: number): number {
    /**
     * Convert an angle from degrees to radians.
     *
     * @param degrees - The angle in degrees to convert.
     * @returns The angle in radians.
     */
    const radians = degrees * (PI / 180);
    return radians;
}