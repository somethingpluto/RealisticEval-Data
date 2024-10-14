import { PI } from "mathjs";

function radiansToDegrees(radians: number): number {
    const degrees = radians * (180 / PI);
    return degrees;
}
