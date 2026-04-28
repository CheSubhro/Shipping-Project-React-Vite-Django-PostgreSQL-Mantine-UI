
import { useState } from 'react';
import { 
  Container, TextInput, NumberInput, Button, 
  Paper, Title, Text, Group, Stack, Card, Badge, Divider 
} from '@mantine/core';
import { IconTruckDelivery, IconMapPin, IconWeight } from '@tabler/icons-react';
import axios from 'axios';

function App() {

	const [loading, setLoading] = useState(false);
	const [formData, setFormData] = useState({
		source_city: '',
		destination_city: '',
		weight_kg: 1
	});
	const [result, setResult] = useState(null);

	const handleCalculate = async () => {
		setLoading(true);
		try {
		const response = await axios.post('http://127.0.0.1:8000/api/shipping/calculate/', formData);
		setResult(response.data);
		} catch (error) {
		alert("Error calculating shipping. Please check if backend is running.");
		console.error(error);
		} finally {
		setLoading(false);
		}
	};

	return (
		<Container size="sm" py={50}>
		<Paper shadow="md" p={30} radius="md" withBorder>
			<Stack align="center" mb={30}>
			<IconTruckDelivery size={50} color="blue" />
			<Title order={2}>Quick Shipping Calculator</Title>
			<Text c="dimmed" size="sm">Get real-time road distance and cost estimation</Text>
			</Stack>

			<Stack spacing="md">
			<TextInput
				label="Source City"
				placeholder="e.g. Kolkata"
				icon={<IconMapPin size={16} />}
				value={formData.source_city}
				onChange={(e) => setFormData({ ...formData, source_city: e.target.value })}
			/>

			<TextInput
				label="Destination City"
				placeholder="e.g. Delhi"
				icon={<IconMapPin size={16} />}
				value={formData.destination_city}
				onChange={(e) => setFormData({ ...formData, destination_city: e.target.value })}
			/>

			<NumberInput
				label="Weight (kg)"
				placeholder="Package weight"
				precision={2}
				icon={<IconWeight size={16} />}
				value={formData.weight_kg}
				onChange={(val) => setFormData({ ...formData, weight_kg: val })}
			/>

			<Button 
				fullWidth 
				size="lg" 
				mt="md" 
				loading={loading}
				onClick={handleCalculate}
			>
				Calculate Now
			</Button>
			</Stack>

			{result && (
			<Card withBorder padding="lg" radius="md" mt={30} bg="blue.0">
				<Group position="apart">
				<Text size="lg" weight={700}>Calculation Summary</Text>
				<Badge color="blue" variant="filled">Success</Badge>
				</Group>

				<Divider my="sm" />

				<Stack spacing="xs">
				<Group position="apart">
					<Text size="sm">Distance:</Text>
					<Text weight={600}>{result.distance}</Text>
				</Group>

				<Group position="apart">
					<Text size="xl" color="blue" weight={700}>Total Cost:</Text>
					<Text size="xl" color="blue" weight={900}>{result.total_cost}</Text>
				</Group>
				</Stack>
			</Card>
			)}
		</Paper>
		</Container>
	);
}

export default App;