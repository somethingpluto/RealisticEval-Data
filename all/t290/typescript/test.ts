describe('rdfJsonLdToNgsiLd', () => {
  it('should convert RDF JSON-LD to NGSI-LD', () => {
    const rdfJsonLd = '{...}'; // Replace with your actual RDF JSON-LD input
    const expectedOutput: any = {...}; // Replace with your expected output based on the NGSI-LD format

    const result = rdfJsonLdToNgsiLd(rdfJsonLd);

    expect(result).toEqual(expectedOutput);
  });
});