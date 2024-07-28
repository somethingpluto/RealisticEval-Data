double Circle::intersectionArea(const Circle & otherCircle) {
  double d = center.distanceFrom(otherCircle.center);
  double r1 = radius;
  double r2 = otherCircle.radius;

  if (d >= r1 + r2) {
    // circles are separate
    return 0.0;
  }
  else if (d <= std::abs(r1 - r2)) {
    // one circle is inside the other
    return M_PI * std::min(r1, r2) * std::min(r1, r2);
  }
  else {
    // partial overlap
    double a1 = r1 * r1 * std::acos((d * d + r1 * r1 - r2 * r2) / (2 * d * r1));
    double a2 = r2 * r2 * std::acos((d * d + r2 * r2 - r1 * r1) / (2 * d * r2));
    double a3 =
        0.5 * std::sqrt((-d + r1 - r2) * (-d - r1 + r2) * (-d + r1 + r2) * (d + r1 + r2));
    return a1 + a2 - a3;
  }
}