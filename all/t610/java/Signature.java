/**
 * Rewrite the hashcode method in the content part of the class so that its hashcode is related to the name and age fields in the class
 *
 * @return obj hashcode
 */
@Override
public int hashCode() {
    final int prime = 31;
    int result = 1;

    // Calculate hash code based on name
    result = prime * result + (name == null ? 0 : name.hashCode());

    // Calculate hash code based on age
    result = prime * result + age;

    return result;
}