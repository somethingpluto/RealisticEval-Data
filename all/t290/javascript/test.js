describe('RDF JSON-LD to NGSI-LD Conversion', () => {
  it('should convert RDF JSON-LD to NGSI-LD correctly', () => {
    const rdfJsonLd = `
      {
        "@context": "http://www.w3.org/ns/jsonld#",
        "@type": "Question",
        "name": "What is the capital of France?",
        "answer": "Paris"
      }
    `;

    const expectedNgsiLD = {
      id: expect.any(String),
      type: 'Question',
      name: 'What is the capital of France?',
      answer: 'Paris'
    };

    const result = rdfJsonLdToNgsiLD(rdfJsonLd);

    expect(result).toEqual(expectedNgsiLD);
  });

  it('should handle empty input gracefully', () => {
    const rdfJsonLd = '';

    const expectedNgsiLD = {};

    const result = rdfJsonLdToNgsiLD(rdfJsonLd);

    expect(result).toEqual(expectedNgsiLD);
  });
});