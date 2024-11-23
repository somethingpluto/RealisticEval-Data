import { pi } from "mathjs";

function radiansToDegrees(radians: number): number {
    const degrees = radians * (180 / pi);
    return degrees;
}
