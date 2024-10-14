import { PI } from "mathjs";

function degreesToRadians(degrees: number): number {
    const radians = degrees * (PI / 180);
    return radians;
}