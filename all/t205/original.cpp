static string getYYYYMMDD()
{
  time_t now = time(0);
  struct tm tm;
  localtime_r(&now, &tm);
  char tmp[80];
  strftime(tmp, sizeof(tmp), "%Y-%m-%d", &tm);
  return tmp;
}
